json.(user, :id, :email, :name, :image_url, :created_at, :updated_at)
json.token user.generate_jwt