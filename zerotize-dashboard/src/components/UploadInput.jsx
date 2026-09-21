import { Form, Button } from "react-bootstrap";

/**
 * UploadInput
 * Input group used for image/file upload fields.
 * - Left: text input (shows selected filename or placeholder)
 * - Right: Browse button that triggers a hidden file input
 * - Matches the "Advertisement image" / "Attachment" rows in the screenshots
 */
export default function UploadInput({ label, placeholder, value, onChange, onBrowse, name, accept }) {
  const fakeRef = React.useRef(null);
  const [fileName, setFileName] = React.useState(value || "");

  const handleFile = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      setFileName(file.name);
      onChange?.(file);
    }
  };

  return (
    <div className="mb-3">
      <div className="zt-field-label">{label}</div>
      <div className="upload-input-group">
        <Form.Control
          type="text"
          className="upload-value"
          placeholder={placeholder}
          readOnly
          value={fileName || ""}
          style={{ cursor: "default" }}
        />
        <Button
          type="button"
          variant="outline-secondary"
          className="upload-browse"
          onClick={() => fakeRef.current?.click()}
        >
          Browse
        </Button>
        <input
          ref={fakeRef}
          type="file"
          name={name}
          accept={accept || "image/*"}
          className="d-none"
          onChange={handleFile}
        />
      </div>
    </div>
  );
}
