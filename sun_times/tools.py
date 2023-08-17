import requests
import rich


def get_sun_time_from_coordinates(*, lat, lng):
    r = requests.get(f"https://api.sunrisesunset.io/json?lat={lat}&lng={lng}")
    sunrise = r.json()["results"]["sunrise"]
    sunset = r.json()["results"]["sunset"]
    sun_times = {"sunrise": sunrise, "sunset": sunset}
    return sun_times


rich.print(get_sun_time_from_coordinates(lat=51.50853, lng=-0.12574))
