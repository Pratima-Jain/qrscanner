



# 🔗 QR Code Generator
---

## 🧠 About This Project

Welcome! 👋
This is a **minimal yet powerful Python script** that instantly generates a **QR code** linking directly to my GitHub Profile.

Whether you're attending an event, submitting a resume, or building your digital portfolio — this little utility helps you share your profile with just one scan 📱.

---

## ✨ Features

✅ Lightweight & Fast
✅ No GUI — just run and get your PNG
✅ Perfect for resumes, business cards, banners, etc.
✅ Clean and customizable output file

---

## 💻 Technologies Used

* **Python 3**
* [`qrcode`](https://pypi.org/project/qrcode/) library (with PIL backend)

---

## 🧾 The Code

```python
import qrcode  # type: ignore

myqr = qrcode.make("https://github.com/Pratima-Jain?tab=repositories")
myqr.save("Pratima Jain_GitHub.png")
```

> 🖼️ Output: A file named `Pratima Jain_GitHub.png` will be generated in your working directory.

---

## 🚀 Getting Started

### 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/Pratima-Jain/<your-repo-name>.git
cd <your-repo-name>
```

2. Install dependencies:

```bash
pip install qrcode[pil]
```

3. Run the script:

```bash
python your_script_name.py
```

4. Done! 🎉
   Your QR code image will appear in the same folder as `Pratima Jain_GitHub.png`.

---

## 📸 Preview

<div align="center">
  <img src="Pratima%20Jain_GitHub.png" alt="QR Code" width="200"/>
  <br/>
  <i>Scan me to visit my GitHub repositories!</i>
</div>

---

## 💡 Use Cases

✨ Add to your **resume**
✨ Embed in your **portfolio**
✨ Use on **event posters**
✨ Share easily during **networking sessions**
✨ Add to **business cards**

---

## 🙋‍♀️ About Me

Hi, I’m **[Pratima Jain](https://github.com/Pratima-Jain)** 👩‍💻
I'm passionate about building, learning, and sharing tools that make tech more accessible and impactful.

---

## 📫 Connect with Me

* [GitHub](https://github.com/Pratima-Jain)
* [LinkedIn](www.linkedin.com/in/pratimajain06) 


---

> ⭐ If you liked this project, consider giving it a star on GitHub!


