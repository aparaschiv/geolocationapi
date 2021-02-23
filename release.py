import io
import os
import shutil
import tarfile
import requests

GEOIP2_DB_URL = (
    "https://download.maxmind.com/app/geoip_download_by_token?edition_id=GeoLite2-Country&date=20210216&suffix=tar.gz&token=v2.local.-d-riKV1RoY4C8GW92VRsI-4y08Ol3zLQd0e5MX2--Vs_YoA9agDe-OlbIFl5xuCbAEJFlQrwE9OEYjutwQAw-L9D-sVfvXukZVN0zY13L18xVGs3zypiOGGNMP099hF5IdwUhtCX0iT2FIxOoO7MhN-ouywKrwJrzxp89Dv84Yk1YLiRRCwIIIrMRYxnNldoH3lJg"
)

r = requests.get(GEOIP2_DB_URL)
tar = tarfile.open(mode="r:gz", fileobj=io.BytesIO(r.content))
for member in tar.getmembers():
    if member.name.endswith("GeoLite2-Country.mmdb"):
        member.name = os.path.basename(member.name)
        tar.extract(member, path="data")
