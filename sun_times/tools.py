import requests
import rich


def sun_time(lat, lng):
    r = requests.get(f"https://api.sunrisesunset.io/json?lat={lat}&lng={lng}")
    sunrise = r.json()["results"]["sunrise"]
    sunset = r.json()["results"]["sunset"]
    sun_times = {"sunrise": sunrise, "sunset": sunset}
    return sun_times


rich.print(sun_time(51.50853, -0.12574))
