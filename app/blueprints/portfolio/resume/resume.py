from flask import Blueprint, render_template

resume_page = Blueprint('resume',
                        __name__,
                        url_prefix='/portfolio',
                        template_folder='templates')


@resume_page.route('/resume')
def resume():
    return render_template('resume.html')
