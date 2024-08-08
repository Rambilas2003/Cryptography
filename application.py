from flask import Flask,render_template, request, url_for, session


app = Flask(__name__,template_folder='templet')
app.secret_key = "hello"

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/enc", methods=["GET", "POST"])
def encryption():
    if request.method == "POST" and 'txt' in request.form:
        txt = str(request.form['txt'])
        session["txt"] = txt
        import appmain,main_genalgo
        key,encrypted_text = appmain.run_encryption(txt)
        print(f'key: {key}\nENC: {encrypted_text}')
        return render_template('index.html', msg=f"Encrypted text: {encrypted_text}",key=f"Key: {key}")
    else:
        return render_template('index.html')

@app.route("/dyc",methods=["GET","POST"])
def decryption():
    if request.method == "POST":
        enc_txt = str(request.form['txt'])
        key = str(request.form['key'])
        session["enc_txt"] = enc_txt
        session["key"] = key
        try:
            import appmain,main_genalgo
            decrypt_text = appmain.run_decrypt(key,enc_txt)
            print(decrypt_text)
            return render_template("index.html",msg1=decrypt_text)
        except:
            return render_template("index.html", msg="Technical Error TryAgain")
    else:
        return render_template("index.html",msg1="ERROR")


   
if __name__ == '__main__':
    app.run(debug=True)