import qrcode  # type: ignore

myqr= qrcode.make("https://github.com/Pratima-Jain?tab=repositories")
myqr.save("Pratima Jain_GitHub.png")

