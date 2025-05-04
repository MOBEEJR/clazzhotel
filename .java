function sanitize(input) {
  return input.replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
