# In Python (Flask), set security headers
from flask import Flask, Response

app = Flask(_name_)

@app.after_request
def set_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'  # HSTS
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevent MIME sniffing
    response.headers['X-Frame-Options'] = 'DENY'  # Prevent clickjacking
    response.headers['X-XSS-Protection'] = '1; mode=block'  # Prevent XSS attacks
    response.headers['Referrer-Policy'] = 'no-referrer-when-downgrade'  # Control referrer information
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none'; style-src 'self';"  # CSP
    return response