import api from "../services/api";

function UploadPage() {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);
    await api.post("upload/", formData);
    window.location.reload();
  };

  return (
    <div className="card upload-box">
      <h3>Upload Equipment CSV</h3>
      <input type="file" accept=".csv" onChange={handleUpload} />
    </div>
  );
}

export default UploadPage;
