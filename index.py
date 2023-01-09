from requests import get


websites = (

  "google.com",

  "airbnb.com",

  "https://twitter.com",

  "facebook.com",

  "https://tiktok.com"

)


results = {

}


#website = placeholder

for website in websites :

  if not website.startswith("https://") :

    website = f"https://{website}"

  response = get(website)

  if response.status_code >=100 and response.status_code:
    print(f"{website}shows 1xx messages")

    results[website] = "Information Response"

  elif response.status_code >=200 and response.status_code:
    print(f"{website}shows 2xx messages")

    results[website] = "Success"

  elif response.status_code >=300 and response.status_code:
    print(f"{website}shows 3xx messages")

    results[website] = "Redirection"

  elif response.status_code >=400 and response.status_code:
    print(f"{website}shows 4xx messages")

    results[website] = "Client Error"

  elif response.status_code >=500 and response.status_code < 600 :

    print(f"{website}shows 5xx messages")

    results[website] = "Server Error"


print(results)