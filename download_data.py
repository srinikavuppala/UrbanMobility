import requests
import os

os.makedirs("data/raw", exist_ok=True)

# --- Download Yellow Taxi Data ---
url1 = "https://d37ci6vzuechgl.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
file1 = "data/raw/yellow_tripdata_2024-01.parquet"

print("Downloading Yellow Taxi Data (Jan 2024)...")
print("File is ~50MB, please wait...")

r1 = requests.get(url1, stream=True)
total1 = int(r1.headers.get('content-length', 0))
done1 = 0

with open(file1, 'wb') as f:
    for chunk in r1.iter_content(chunk_size=1024*1024):
        f.write(chunk)
        done1 += len(chunk)
        pct = (done1 / total1 * 100) if total1 > 0 else 0
        print(f"\r  Progress: {pct:.1f}% ({done1/(1024*1024):.1f} MB)", end="")

print("\n  Taxi data downloaded!")

# --- Download Zone Lookup ---
url2 = "https://d37ci6vzuechgl.cloudfront.net/misc/taxi+_zone_lookup.csv"
print("Downloading Zone Lookup...")
r2 = requests.get(url2)
with open("data/raw/taxi_zone_lookup.csv", 'wb') as f:
    f.write(r2.content)
print("  Zone lookup downloaded!")

# --- Download Shapefile ---
url3 = "https://d37ci6vzuechgl.cloudfront.net/misc/taxi_zones.zip"
print("Downloading Shapefile...")
r3 = requests.get(url3, stream=True)
with open("data/raw/taxi_zones.zip", 'wb') as f:
    for chunk in r3.iter_content(chunk_size=1024*1024):
        f.write(chunk)
print("  Shapefile downloaded!")

# --- Verify ---
print("\nFiles in data/raw/:")
for f in os.listdir("data/raw"):
    size = os.path.getsize(f"data/raw/{f}") / (1024*1024)
    print(f"  {f} ({size:.1f} MB)")

print("\nAll data downloaded! Ready for analysis.")