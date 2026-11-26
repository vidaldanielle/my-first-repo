function Header({ count, total }) {
  return (
    <header>
      <h1>HR Policy Search</h1>
      <p>Nahanap: {count} sa {total}</p>
    </header>
  );
}

export default Header;