function Header({ count }) {
  return (
    <header>
      <h1>HR Policy Search</h1>
      <p>Mga polisiya: {count}</p>
    </header>
  );
}

export default Header;