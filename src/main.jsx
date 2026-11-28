import React from'react';
import{createRoot}from'react-dom/client';
import Painel from'./Painel.jsx';
import './style.css';
import{iniciarAudiencia}from'./audiencia.mjs';
iniciarAudiencia();
createRoot(document.getElementById('root')).render(<Painel/>);
