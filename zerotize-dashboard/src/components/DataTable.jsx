import { Card, Table } from "react-bootstrap";

/**
 * DataTable
 * Renders a mock table inside a card.
 * - Wrapped in a table-responsive with a purple scrollbar
 * - Bold header row
 * - Any cell marked as a "zt-id" is rendered as a purple clickable link
 */
export default function DataTable({ columns, rows, className }) {
  return (
    <Card className={className || ""}>
      <div className="table-responsive">
        <Table className="align-middle mb-0">
          <thead>
            <tr>
              {columns.map((col) => (
                <th key={col.key} style={{ ...col.headerStyle }}>
                  {col.label}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map((row) => (
              <tr key={row.key || row.id}>
                {columns.map((col) => {
                  const value = row[col.keyKey] ?? "";
                  const isId =
                    col.cellType === "zt-id" || col.key === "id" || col.key === "linkId" || col.key === "ticketId";
                  const content = col.render
                    ? col.render(row, value, col)
                    : value;

                  if (isId) {
                    return (
                      <td key={col.key}>
                        <span className="zt-id">{content}</span>
                      </td>
                    );
                  }

                  return (
                    <td key={col.key}>
                      {col.cellType === "rupee"
                        ? (
                          <span className="zt-rupee">₹</span>
                        ) : null}
                      {col.cellType === "rupee" && value ? (
                        <span>{value}</span>
                      ) : col.cellType === "rupee" && !value ? null : (
                        content
                      )}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </Table>
      </div>
    </Card>
  );
}
