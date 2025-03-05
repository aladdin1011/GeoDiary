import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)

function App(){
  return(
    <div>
      <h1> Привет! </h1>
      <button onClick={() => alert("Ты нажал на кнопку")}>Нажми меня</button>
    </div>
  );
}

export default App;