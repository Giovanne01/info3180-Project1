"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from xml.dom.minidom import CDATASection
from app import app
from flask import render_template, request, redirect, url_for,flash, session,send_from_directory
from werkzeug.utils import secure_filename
from app.form import *
from app.models import *
###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

info=[]

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Giovanne Pinto")

@app.route('/properties/create', methods=['POST','GET'])
def create():
    form= CreateProperties()
    if request.method=="POST":

        if form.validate_on_submit():
            photo= form.photo.data
            filename= secure_filename(photo.filename)
            title= form.title.data
            bednum= form.bednum.data
            bathnum= form.bathnum.data
            location= form.location.data
            price= form.price.data
            type= form.type.data
            description= form.description.data
            print('done')

            filename=secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            property=AddProperty(title=title, bednum=bednum,bathnum=bathnum,
                location=location, price=price,type=type, description=description,
                photo=filename)

            db.session.add(property)
            db.session.commit()

            flash('Property was successfully added', 'success')
            print('Done')
            return redirect(url_for('properties'))
        else:
            flash_errors(form)    
    return render_template('create_form.html', form=form)
    
@app.route('/properties')
def properties():
    info= AddProperty.query.all()
    return render_template('properties.html',info=info)

@app.route('/properties/<id>')
def prop1(id):
    data= AddProperty.query.filter_by(id=id).first()

    return render_template('propert.html', data=data)
#FORMS
@app.route('/uploads/<filename>')
def getimage(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

def get_upload_images():
    filename=[]
    rootdir = os.getcwd()
    print (rootdir)
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            filename+=[file]
            print (os.path.join(subdir, file))
    return filename



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
