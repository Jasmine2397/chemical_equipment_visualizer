import api from "../services/api";

function UploadPage() {
  const handleUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);
    await api.post("upload/", formData);
    alert("Uploaded successfully");
  };

  return <input type="file" onChange={handleUpload} />;
}

export default UploadPage;
