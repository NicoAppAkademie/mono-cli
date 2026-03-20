---
layout: default
title: Home
---

<section class="hero">
  <div class="container">
    <p class="hero-badge">v0.1.0 — open source</p>
    <h1>Your personal<br><span>link archive.</span></h1>
    <p class="hero-sub">
      mono is a minimal command-line tool for saving, organizing and
      revisiting URLs with notes — no account, no cloud, just a JSON
      file on your machine.
    </p>
    <div class="btn-group">
      <a class="btn btn-primary" href="#install">Get started →</a>
      <a class="btn btn-secondary" href="https://github.com/NicoAppAkademie/mono-cli" target="_blank" rel="noopener">GitHub ↗</a>
    </div>

    <div class="terminal">
      <span class="prompt">$ </span><span class="cmd">uv run mono</span><br>
      <span class="out">? mono  (Use arrow keys)</span><br>
      <span class="out"> ❯ </span><span class="highlight">Add</span><br>
      <span class="out">   Delete</span><br>
      <span class="out">   Edit</span><br>
      <span class="out">   Exit</span><span class="cursor"></span>
    </div>
  </div>
</section>

<section class="section" id="features">
  <div class="container">
    <p class="section-label">Capabilities</p>
    <h2>Everything you need,<br>nothing you don't.</h2>

    <div class="features-grid">
      <div class="feature-card">
        <span class="feature-icon">+</span>
        <h3>Add</h3>
        <p>
          Paste any URL and attach a short note. mono stores it instantly
          in a local JSON file so you can find it later.
        </p>
      </div>
      <div class="feature-card">
        <span class="feature-icon">−</span>
        <h3>Delete</h3>
        <p>
          Scroll through your saved links with arrow keys and remove
          the ones you no longer need — one keystroke, gone.
        </p>
      </div>
      <div class="feature-card">
        <span class="feature-icon">✎</span>
        <h3>Edit</h3>
        <p>
          Pick any entry from the interactive list and update its URL
          or note without leaving the terminal.
        </p>
      </div>
      <div class="feature-card">
        <span class="feature-icon">↩</span>
        <h3>Exit</h3>
        <p>
          Leave whenever you want. Your data is already written to disk —
          no save step required.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="section" id="install">
  <div class="container">
    <p class="section-label">Installation</p>
    <h2>Up and running<br>in seconds.</h2>
    <p>mono requires <strong>Python 3.13+</strong> and <a href="https://github.com/astral-sh/uv" target="_blank" rel="noopener">uv</a>.</p>

    <div class="terminal">
      <span class="prompt comment"># Clone the repository</span><br>
      <span class="prompt">$ </span><span class="cmd">git clone https://github.com/NicoAppAkademie/mono-cli.git</span><br>
      <span class="prompt">$ </span><span class="cmd">cd mono-cli</span><br><br>
      <span class="prompt comment"># Install dependencies</span><br>
      <span class="prompt">$ </span><span class="cmd">uv sync</span><br><br>
      <span class="prompt comment"># Run mono</span><br>
      <span class="prompt">$ </span><span class="cmd">uv run mono</span><span class="cursor"></span>
    </div>
  </div>
</section>

<section class="section" id="usage">
  <div class="container">
    <p class="section-label">Usage</p>
    <h2>How it works.</h2>
    <p>
      mono presents an interactive menu each time you run it.
      Navigate with the <code>↑ ↓</code> arrow keys and press
      <code>Enter</code> to select an action.
    </p>

    <div class="terminal">
      <span class="prompt comment"># Adding a link</span><br>
      <span class="prompt">$ </span><span class="cmd">uv run mono</span><br>
      <span class="out">? mono  Add</span><br>
      <span class="out">? URL:  </span><span class="cmd">https://example.com/article</span><br>
      <span class="out">? Note: </span><span class="cmd">Great read on distributed systems</span><br>
      <span class="highlight">✔ Saved: https://example.com/article</span>
    </div>

    <p>Links are persisted in <code>~/.mono/links.json</code> and look like this:</p>

    <div class="data-example">[<br>
  &nbsp;&nbsp;{<br>
  &nbsp;&nbsp;&nbsp;&nbsp;"url": "https://example.com/article",<br>
  &nbsp;&nbsp;&nbsp;&nbsp;"note": "Great read on distributed systems"<br>
  &nbsp;&nbsp;}<br>
]</div>

    <p style="margin-top:1.5rem;">
      No external services. No tracking. Your links live entirely on your machine.
    </p>
  </div>
</section>
