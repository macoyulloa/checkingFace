class UsersController < ApplicationController
    before_action :authenticate_user!, except: [:index]

    def index
        @users = User.all
        render json: @users
    end

    def show        
    end

    def update
        if current_user.update_attributes(user_params)
             render :show
        else
            render json: { errors: current_user.errors }, status: :unprocessable_entity
        end
    end

    private

    def user_params
        params.require(:user).permit(:name, :email, :image_url, :password)
    end
end
