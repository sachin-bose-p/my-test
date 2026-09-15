import './style.css';
import heroImg from './assets/hero.png';
import typescriptLogo from './assets/typescript.svg';
import viteLogo from './assets/vite.svg';
import { setupCounter } from './counter.ts';
import { Provider } from 'react-redux';
import store from './store';
import AppRoutes from './routes/index';

// Simplify into a single App component with correct JSX
const App = () => (
  <Provider store={store}>
    <AppRoutes />
    <MainSection />
  </Provider>
);

// Correcting the duplicate App component definition and JSX placement
const App: React.FC = () => (
  <Provider store={store}>
    <AppRoutes />
  </Provider>
);


const MainSection: React.FC = () => (
  <section id="center">
    <div className="hero">
      <img src={heroImg} className="base" width="170" height="179" alt="Hero" />
      <img src={typescriptLogo} className="framework" alt="TypeScript logo" />
      <img src={viteLogo} className="vite" alt="Vite logo" />
    </div>
    <div>
      <h1>Get started</h1>
      <p>Edit <code>src/main.ts</code> and save to test <code>HMR</code></p>
    </div>
    <button id="counter" type="button" className="counter">Count</button>
  </section>
);

setupCounter(document.querySelector<HTMLButtonElement>('#counter')!);

const MainSection = () => (
  <section id="center">
    <div className="hero">
      <img src={heroImg} className="base" width="170" height="179" />
      <img src={typescriptLogo} className="framework" alt="TypeScript logo" />
      <img src={viteLogo} className="vite" alt="Vite logo" />
    </div>
    <div>
      <h1>Get started</h1>
      <p>Edit <code>src/main.ts</code> and save to test <code>HMR</code></p>
    </div>
    <button id="counter" type="button" className="counter"></button>
  </section>
);


setupCounter(document.querySelector<HTMLButtonElement>('#counter')!);

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
<section id="center">
  <div class="hero">
    <img src="${heroImg}" class="base" width="170" height="179">
    <img src="${typescriptLogo}" class="framework" alt="TypeScript logo"/>
    <img src="${viteLogo}" class="vite" alt="Vite logo" />
  </div>
  <div>
    <h1>Get started</h1>
    <p>Edit <code>src/main.ts</code> and save to test <code>HMR</code></p>
  </div>
  <button id="counter" type="button" class="counter"></button>
</section>

<div class="ticks"></div>

<section id="next-steps">
  <div id="docs">
    <svg class="icon" role="presentation" aria-hidden="true"><use href="/icons.svg#documentation-icon"></use></svg>
    <h2>Documentation</h2>
    <p>Your questions, answered</p>
    <ul>
      <li>
        <a href="https://vite.dev/" target="_blank">
          <img class="logo" src="${viteLogo}" alt="" />
          Explore Vite
        </a>
      </li>
      <li>
        <a href="https://www.typescriptlang.org" target="_blank">
          <img class="button-icon" src="${typescriptLogo}" alt="">
          Learn more
        </a>
      </li>
    </ul>
  </div>
  <div id="social">
    <svg class="icon" role="presentation" aria-hidden="true"><use href="/icons.svg#social-icon"></use></svg>
    <h2>Connect with us</h2>
    <p>Join the Vite community</p>
    <ul>
      <li><a href="https://github.com/vitejs/vite" target="_blank"><svg class="button-icon" role="presentation" aria-hidden="true"><use href="/icons.svg#github-icon"></use></svg>GitHub</a></li>
      <li><a href="https://chat.vite.dev/" target="_blank"><svg class="button-icon" role="presentation" aria-hidden="true"><use href="/icons.svg#discord-icon"></use></svg>Discord</a></li>
      <li><a href="https://x.com/vite_js" target="_blank"><svg class="button-icon" role="presentation" aria-hidden="true"><use href="/icons.svg#x-icon"></use></svg>X.com</a></li>
      <li><a href="https://bsky.app/profile/vite.dev" target="_blank"><svg class="button-icon" role="presentation" aria-hidden="true"><use href="/icons.svg#bluesky-icon"></use></svg>Bluesky</a></li>
    </ul>
  </div>
</section>

<div class="ticks"></div>
<section id="spacer"></section>
`;

setupCounter(document.querySelector<HTMLButtonElement>('#counter')!);
