from typing import Optional

import typer

from find_nearest_restaurants import K_LESS_0, K_NOT_INT, LATITUDE_OUT_OF_RANGE, LONGITUDE_OUT_OF_RANGE, __app_name__, __version__, ERRORS
from find_nearest_restaurants.find_restaurants import food_truck_finder

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),

) -> None:
    return


@app.command()
def find(
    latitude: float = typer.Argument(...,
        help = "Latitude of your location"
    ),

    longitude: float = typer.Argument(...,
        help = "Longitude of your location"
    ),

    k: int = typer.Argument(...,
        help = "Number of restaurants to be displayed"
    )
):
    if k <= 0:
        typer.secho(ERRORS[K_LESS_0] + ": {k}".format(k=k))
        raise typer.Exit(1)
    
    if not isinstance(k, int):
        typer.secho(ERRORS[K_NOT_INT] + ": {k}".format(k=k))
        raise typer.Exit(1)

    try:
        assert latitude <= 90 and latitude >= -90
    except:
        typer.secho(ERRORS[LATITUDE_OUT_OF_RANGE] + ": {latitude}".format(latitude=latitude))
        raise typer.Exit(2)
    
    try:
        assert longitude <= 180 and longitude >= -180
    except:
        typer.secho(ERRORS[LONGITUDE_OUT_OF_RANGE] + ": {longitude}".format(longitude=longitude))
        raise typer.Exit(3)

    coordinates = (latitude, longitude)
    
    food_truck_finder_object = food_truck_finder(coordinates, k)
    locations = food_truck_finder_object.get_pd_dataframe_top_k()
    locations
    typer.secho(locations)
