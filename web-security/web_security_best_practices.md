# Web Security Testing

Note: The resources below are free or open-source.

## Web Vulnerability Scanning

- Reference: **OWASP** - Read more: <https://owasp.org/>
- **OWASP ZAP** (Zed Attack Proxy): <https://www.zaproxy.org/>

## SSL/TLS Configuration Test

Qualys SSL Lab: https://www.ssllabs.com/ssltest/

## Code Scanning

- Reference by GitHub: <https://docs.github.com/en/code-security/code-scanning>
- Dependabot by GitHub: <https://github.com/dependabot>
- CodeQL by GitHub: <https://codeql.github.com/>

## Check dependencies for known vulnerabilities

Purpose: Scanning third-party libraries and frameworks for known vulnerabilities

- Snyk (link to GitHub, free for individual developer): <https://snyk.io/>
- OWASP Dependency-Check
- npm audit (for Node.js projects)

## Security Headers

Purpose: Scanning your website and suggest improvements.

- SecurityHeaders: <https://securityheaders.com/>
  - Once we get the results from SecurityHeaders, we can edit the `.htaccess` file to improve the headers.
  - If you're using Hostinger like me, please check out their instructions at: <https://www.hostinger.com/tutorials/locate-and-create-htaccess>
  - Open the .htaccess file for editing. You can do this by selecting the file and looking for an edit option.
  - Add the recommended headers to your .htaccess file by copying and pasting the following lines:
  ```
    # Strict-Transport-Security
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
    # X-Frame-Options
    Header always set X-Frame-Options "SAMEORIGIN"
    # X-Content-Type-Options
    Header always set X-Content-Type-Options "nosniff"
    # Referrer-Policy
    Header always set Referrer-Policy "no-referrer-when-downgrade"
    # Permissions-Policy
    # Example: Disable geolocation and microphone for the entire site
    Header always set Permissions-Policy "geolocation=(), microphone=()"
  ```
