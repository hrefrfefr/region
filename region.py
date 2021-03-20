from Samples.geocoder import geocode


def get_address_component(town, component_index):
    toponym = geocode(town)
    components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    return components[component_index]["name"]


def main():
    for town in ["Барнаул", "Мелеуз", "Йошкар-Ола"]:
        area = get_address_component(town, 2)
        print(f"{town}: {area}")
    print("")


if __name__ == "__main__":
    main()