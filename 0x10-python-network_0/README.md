# 0x10. Python - Network #0

## 1. URL (Uniform Resource Locator)

A URL is a string of characters used to address resources on the web. It typically consists of a protocol (such as HTTP or HTTPS), followed by a domain name or IP address, and optionally, a path to a specific resource on the server.

## 2. HTTP (Hypertext Transfer Protocol)

HTTP is a protocol that governs the communication between web clients (such as browsers) and web servers. It defines how messages are formatted and transmitted, as well as how web servers and clients respond to various commands.

## 3. How to read a URL

To read a URL, you typically start by identifying the protocol (e.g., HTTP), followed by the domain name or IP address, then any optional port number, path, and query string parameters.

## 4. Scheme for an HTTP URL
The scheme for an HTTP URL indicates the protocol being used, such as "http://" or "https://".

## 5. Domain name

A domain name is a human-readable label that corresponds to a unique IP address on the internet. It's used to identify specific websites and resources.

## 6. Sub-domain

A sub-domain is a subsection of a larger domain. It precedes the main domain name and often represents a specific branch or section of a website.

## 7. Port number in a URL

Port numbers in a URL specify the endpoint of communication on the server. They are separated from the domain name by a colon, e.g., "http://example.com:8080".

## 8. Query string

A query string is a part of a URL that contains data to be passed to the server as key-value pairs. It begins with a question mark and can include multiple parameters separated by ampersands.

## 9. HTTP request

An HTTP request is a message sent by a client (such as a web browser) to a server, requesting a specific action, such as retrieving a web page or submitting form data.

## 10. HTTP response

An HTTP response is a message sent by a server to a client in response to an HTTP request. It contains the requested resource or information about the outcome of the request.

## 11. HTTP headers

HTTP headers are additional information sent along with HTTP requests or responses. They contain metadata about the message, such as the content type, encoding, and caching directives.

## 12. HTTP message body

The HTTP message body contains the actual content of the request or response, such as HTML, JSON, or binary data.

## 13. HTTP request method

The HTTP request method specifies the action to be performed on the resource identified by the URL. Common methods include GET (retrieve data), POST (submit data), PUT (update data), and DELETE (remove data).

## 14. HTTP response status code

The HTTP response status code indicates the outcome of the request. It's a three-digit code sent by the server, such as 200 for a successful response or 404 for "Not Found".

## 15. HTTP Cookie

An HTTP cookie is a small piece of data sent from a website and stored on the user's device by the web browser. It's often used for session management, user authentication, and tracking.

## 16. Making a request with cURL

cURL is a command-line tool for transferring data with URLs. To make a request with cURL, you specify the URL and any additional options, such as headers or request methods, in the command line.

## 17. Typing google.com in your browser (Application level)

When you type "google.com" in your browser and press Enter, the browser sends an HTTP request to the server associated with the domain name "google.com". The server then responds with the Google homepage, which the browser renders and displays to the user. This process involves DNS resolution to translate the domain name into an IP address, establishing an HTTP connection, sending the request, receiving the response, and rendering the page.

