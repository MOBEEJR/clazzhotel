<script>
document.getElementById("inquiry-form").addEventListener("submit", function(e) {
  e.preventDefault();

  let name = document.getElementById("name").value.trim();
  let email = document.getElementById("email").value.trim();
  let message = document.getElementById("message").value.trim();

  if (!name || !email || !message) {
    alert("Please fill in all fields.");
    return;
  }

  const whatsappMessage = Hello CLAZZ HOTEL,%0AMy name is ${name}.%0AEmail: ${email}%0AMessage: ${message};
  const whatsappNumber = "234XXXXXXXXXX"; // Replace with your CLAZZ WhatsApp number (remove + and start with 234)

  window.open(https://wa.me/${whatsappNumber}?text=${whatsappMessage}, '_blank');
});
</script>