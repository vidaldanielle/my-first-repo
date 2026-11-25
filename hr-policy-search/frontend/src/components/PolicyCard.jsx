/*Magdagdag ng bagong prop sa PolicyCard, halimbawa effectiveDate, 
at ilagay ang petsa sa data at sa card.
*/
function PolicyCard({ title, category, effectiveDate }) {
  return (
    <li className="policy-card">
      <h3>{title}</h3>
      <span className="badge">{category}</span>
      <p className="effective-date">Effective Date: {effectiveDate}</p>
    </li>
    
  );
}

export default PolicyCard;