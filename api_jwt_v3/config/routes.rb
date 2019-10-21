Rails.application.routes.draw do
  #get 'uploads/new'
  #get 'uploads/create'
  #get 'uploads/index'
  root 'uploads#new'
  scope :api, defaults: {format: :json} do
    devise_for :users, controllers: { sessions: :sessions },
              path_names: { sign_in: :login }

    resource :user, only: [:show, :update]
    get "/all", to: "users#index"
  end
  resources :uploads
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
end
