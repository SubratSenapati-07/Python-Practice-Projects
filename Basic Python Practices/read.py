import http.client


conn = http.client.HTTPSConnection("www.uci.edu")


conn.request("GET", "/")

response = conn.getresponse()

data = response.read().decode()

# Print first 3 lines
lines = data.split("\n")
for i in range(3):
    print(lines[i])
