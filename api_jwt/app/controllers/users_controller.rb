class UsersController < ApplicationController
    before_action :authenticate_user!

    def index
        @users = User.All 
        render json: @users    
    end

    private

    def user_params
        params.require(:user).permit(:name, :image_url)
    end
end
