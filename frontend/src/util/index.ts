export const blobToBase64 = blob => new Promise((resolve, reject) => {
  const reader = new FileReader();
  reader.onerror = reject;
  reader.onload = () => resolve(reader.result);
  reader.readAsDataURL(blob);
})

export const URLToBase64 = async (URL) => {
  const blob = await fetch(URL).then(res => res.blob());
  return await blobToBase64(blob).then(res => res);
}