import terrascript
import terrascript.provider
import terrascript.resource
import terrascript.data

config = terrascript.Terrascript()

# Google Cloud Compute provider
config += terrascript.provider.google(
    credentials='${file("account.json")}', project="myproject", region="us-central1"
)

# Google Compute Image (Debian 9) data source
config += terrascript.data.google_compute_image("image", family="debian-9")

# Add Google Compute Instance resource
config += terrascript.resource.google_compute_instance(
    "myinstance",
    name="myinstance",
    machine_type="n1-standard-1",
    zone="us-central1-a",
    boot_disk={
        "initialize_params": {"image": "data.google_compute_image.image.self_link"}
    },
    network_interface={"network": "default", "access_config": {}},
)
