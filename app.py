from flask import Flask, render_template, request, redirect, url_for, Response
from database import fs, db

app = Flask(__name__)


@app.route("/")
def home():
    images = list(db.images.find().sort("_id", -1))

    return render_template("home.html", images=images)


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["image"]

    if file and file.filename:

        file_id = fs.put(
            file,
            filename=file.filename,
            content_type=file.content_type
        )

        print("Image saved:", file_id)

    return redirect(url_for("home"))


@app.route("/image/<file_id>")
def get_image(file_id):

    from bson import ObjectId

    image = fs.get(ObjectId(file_id))

    return Response(
        image.read(),
        mimetype=image.content_type
    )


if __name__ == "__main__":
    app.run(debug=True)