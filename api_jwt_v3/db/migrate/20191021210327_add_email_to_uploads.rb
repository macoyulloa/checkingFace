class AddEmailToUploads < ActiveRecord::Migration[6.0]
  def change
    add_column :uploads, :email, :string
  end
end
