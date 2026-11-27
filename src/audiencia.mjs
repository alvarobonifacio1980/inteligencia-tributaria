// Integração isolada: nenhuma dependência do painel em disponibilidade do coletor.
export const CHAVE_AUDIENCIA='inteligencia-tributaria.audiencia';
const abas={executiva:[],diagnostico:['creditos','resultado','caixa','dva','riscos','historico'],eficiencia:['investimentos','beneficios'],reforma:['agenda','matriz'],cenarios:['creditos','reforma','capex','contratos','projetos'],fontes:[],sobre:[]};
export function rotaPublica(hash=''){
 const [m,t]=hash.replace(/^#/,'').split('/'); const modulo=Object.hasOwn(abas,m)?m:'executiva';
 const tab=abas[modulo].includes(t)?t:abas[modulo][0];return modulo+(tab?'/'+tab:'');
}
export function origemPublica(referrer){try{return new URL(referrer).origin}catch{return ''}}
export function permitido(env,config){
 try{return config.enabled===true&&/^[0-9a-f]{8}-[0-9a-f-]{27}$/i.test(config.websiteId)&&env.location.hostname===config.hostname&&env.location.pathname.startsWith(config.basePath)&&!env.navigator.webdriver&&!env.navigator.globalPrivacyControl&&env.navigator.doNotTrack!=='1'&&env.localStorage.getItem('umami.disabled')!=='1'&&env.localStorage.getItem(CHAVE_AUDIENCIA)==='permitido'&&!new URLSearchParams(env.location.search).has('sem_estatisticas')}catch{return false}
}
export function payloadSeguro(config,env,rota,nome){
 return {website:config.websiteId,hostname:config.hostname,language:env.navigator.language,screen:`${env.screen.width}x${env.screen.height}`,url:config.basePath+'#'+rotaPublica('#'+rota),title:'Inteligência Tributária · '+rotaPublica('#'+rota),referrer:origemPublica(env.document.referrer),...(nome?{name:nome}:{})};
}
const acoes=new Set(['simulador_acesso','simulador_interacao','cenario_predefinido','business_case','metodologia','fonte','exportar_csv','imprimir','repositorio']);
export function criarColetor({send,clock=()=>Date.now(),route=()=>''}){
 let ultimaRota=null;const ultimos=new Map();
 return {pagina(){const r=rotaPublica('#'+route());if(r===ultimaRota)return;ultimaRota=r;send(r);if(r.startsWith('cenarios/')&&r!=='cenarios/projetos')this.evento('simulador_acesso');if(r==='cenarios/projetos')this.evento('business_case')},evento(acao){if(!acoes.has(acao))return;const r=rotaPublica('#'+route()),key=acao+':'+r,agora=clock(),intervalo=acao==='simulador_interacao'?30000:1000;if(ultimos.has(key)&&agora-ultimos.get(key)<intervalo)return;ultimos.set(key,agora);send(r,acao+':'+r)}};
}
export function preferenciaAudiencia(){try{return window.localStorage.getItem(CHAVE_AUDIENCIA)||'pendente'}catch{return 'negado'}}
export function definirAudiencia(valor){try{window.localStorage.setItem(CHAVE_AUDIENCIA,valor);window.dispatchEvent(new Event('audiencia-preferencia'))}catch{/* armazenamento indisponível: coleta permanece desativada */}}
let instalado=false;
export function iniciarAudiencia(){
 if(instalado)return;instalado=true;
 const env=window;let config=null,coletor=null,ativo=false,script=null,timer=null;
 const send=(rota,nome)=>{if(!ativo||!permitido(env,config))return;try{const p=env.umami?.track(payloadSeguro(config,env,rota,nome));p?.catch?.(()=>{})}catch{/* falha não afeta aplicação */}};
 const parar=()=>{ativo=false;coletor=null;script?.remove();script=null;clearTimeout(timer)};
 const sincronizar=()=>{
  if(!config||!permitido(env,config)){parar();return}if(script)return;
  const rota=()=>rotaPublica(env.location.hash);coletor=criarColetor({send,route:rota});
  // Manual: só enviamos campos permitidos, sem URL livre, query, valores ou identificação.
  script=env.document.createElement('script');script.src=config.scriptUrl;script.async=true;script.referrerPolicy='no-referrer';
  script.dataset.websiteId=config.websiteId;script.dataset.autoTrack='false';script.dataset.autoPageview='false';script.dataset.doNotTrack='true';script.dataset.excludeSearch='true';script.dataset.excludeHash='true';script.dataset.domains=config.hostname;
  script.dataset.beforeSend='filtrarAudiencia';
  env.filtrarAudiencia=(type,payload)=>{if(!ativo||!permitido(env,config)||type!=='event')return null;return payloadSeguro(config,env,rota(),typeof payload.name==='string'&&/^[a-z_]+:[a-z/]+$/.test(payload.name)?payload.name:undefined)};
  script.onload=()=>{if(!permitido(env,config)){parar();return}ativo=true;coletor?.pagina()};script.onerror=parar;env.document.head.append(script);
 };
 env.addEventListener('audiencia-preferencia',sincronizar);
 env.addEventListener('storage',sincronizar);
 env.addEventListener('hashchange',()=>{clearTimeout(timer);timer=env.setTimeout(()=>coletor?.pagina(),0)});
 env.addEventListener('beforeprint',()=>coletor?.evento('imprimir'));
 env.document.addEventListener('change',e=>{if(rotaPublica(env.location.hash).startsWith('cenarios/')&&e.target?.matches?.('input,select'))coletor?.evento('simulador_interacao')});
 env.document.addEventListener('click',e=>{
  const el=e.target?.closest?.('a,button,summary');if(!el)return;
  const r=rotaPublica(env.location.hash);if(el.matches('.adaptation-link')){coletor?.evento('metodologia');return}
  if(el.matches('summary')&&r==='cenarios/projetos'&&!el.parentElement.open){coletor?.evento('business_case');return}
  if(el.tagName==='A'){
   const href=el.getAttribute('href')||'';
   if(href==='https://github.com/alvarobonifacio1980/inteligencia-tributaria')coletor?.evento('repositorio');
   else if(el.closest('.card-source,.reference-card')&&href.startsWith('https://'))coletor?.evento('fonte');
   return;
  }
  // Texto usado apenas para classificar ações fixas do código; nunca enviado.
  const text=el.textContent||'';
  if(text.startsWith('Exportar'))coletor?.evento('exportar_csv');
  else if(r.startsWith('cenarios/')&&/^(Conservador|Intermediário|Otimizado|Usar |Restaurar )/.test(text))coletor?.evento('cenario_predefinido');
 });
 // Configuração pública contém somente ID de coleta, jamais credenciais.
 env.fetch('./data/audiencia.json',{cache:'no-store'}).then(r=>r.ok?r.json():null).then(c=>{if(!c||!['https://cloud.umami.is/script.js'].includes(c.scriptUrl))return;config=c;sincronizar()}).catch(()=>{});
}
