class UploadsController < ApplicationController
  def new
  end

  def create
    # puts "este es el bucket", S3_BUCKET.name
    # puts params[:file].instance_variables
    file_path = params[:file].tempfile.path
    
    obj = S3_BUCKET.object(params[:file].original_filename)
    obj.upload_file(file_path, { acl: 'public-read' })
    # obj.write(file: params[:file], acl: :public_read)
    @upload = Upload.new(url: obj.public_url, name: obj.key, email: params[:email])

    if @upload.save
      #user = User.find_by(email: @upload.email)
      #user.update(image_url: @upload.url)
      update_user_email(@upload)
      redirect_to root_path, succes: 'File successfully uploaded'  
    else
      flash.now[:info] = 'There was an error'
      render :new
    end  
  end

  def index
    @uploads = Upload.all
  end
end
