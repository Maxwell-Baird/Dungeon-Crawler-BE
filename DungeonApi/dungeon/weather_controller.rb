class Api::V1::WeatherController < ApplicationController

  def show
    if params[:location].nil?
      render json: {error: "One or more fields are blank"}, status: 401
    else
      if check_location_valid(params[:location])
        geocode = GeocodingService.new
        response = geocode.coordinates(params[:location])
        weather = Weather.new(response)
        render json: WeatherSerializer.new(weather)
      else
        render json: {error: "One or more locations are in an incorrect format"}, status: 402
      end
    end
  end

  private

  def check_location_valid(location)
    location.split(',').length == 2 && location.split(',')[1].length == 2
  end

end
