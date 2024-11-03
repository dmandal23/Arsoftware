from flask import Flask,render_template, request, redirect
app = Flask(__name__)


# Routin Frontend 

# Home Page
@app.route('/')
def index():
    return render_template ('frontend/index.html')

# Blog Post 
@app.route('/blog/list/')
def bloglist():
    return render_template ('frontend/bloglist.html')

# Blog Details
@app.route('/blog-detail/')
def blogdetail():
    return render_template ('frontend/blog-detail.html')


# Career post details
@app.route('/career-detail/')
def careerdetail():
    return render_template ('frontend/career-detail.html')

# SERVICES PAGE
# Web service
@app.route('/services/web/')
def webservices():
    return render_template ('frontend/web-services.html')

# Ui/Ux Design
@app.route('/services/ui/')
def servicesui():
    return render_template ('frontend/services-ui.html')

# Custom Web App
@app.route('/services/custom/')
def customweb():
    return render_template ('frontend/custom-web.html')

# Mobile Development
@app.route('/services/mobile/')
def mobiledevelop():
    return render_template ('frontend/mobile-development.html')

# PRODUCT PAGE
# ar-csm
@app.route('/products/ar-cms/')
def arcms():
    return render_template ('frontend/ar-cms.html')

# ar - asms
@app.route('/products/ar-asms/')
def arasms():
    return render_template ('frontend/ar-asms.html')

# Ar Learning
@app.route('/products/ar-learning/')
def arlerning():
    return render_template ('frontend/ar-learning.html')

# Biog
@app.route('/products/biog/')
def biog():
    return render_template ('frontend/biog.html')

# Career Page
@app.route('/careers/')
def careers():
    return render_template ('frontend/career.html')

# Contact Page
@app.route('/contact/')
def contact():
    return render_template ('frontend/contact.html')

if __name__=='__main__':
    app.run(debug=True)