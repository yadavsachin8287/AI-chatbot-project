import { Routes, Route } from 'react-router-dom';
import Nav from './components/Nav.jsx';
import Chat from './pages/Chat.jsx';
import Blackbox from './pages/Blackbox.jsx';
import './App.css';

export default function App() {
  return (
    <div className="app">
      <Nav />
      <div className="main">
        <Routes>
          <Route path="/chat" element={<Chat />} />
          <Route path="/blackbox" element={<Blackbox />} />
          <Route path="/" element={<Chat />} />
        </Routes>
      </div>
    </div>
  );
}
