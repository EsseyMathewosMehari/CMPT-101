from PIL import Image, ImageDraw

picture = Image.open("broken_600.png")

def fix_frame(file_name):
    
    pic = file_name
    w,h = pic.size 
    imagee = Image.new("RGB", (w, h), (0, 0, 0))
    L = 0
    T =  0
    R = w//2
    B = h//2 
    G = pic.crop((L, T, R, B))
    w_b, h_b = G.size
    L = int(w/2)
    T =  0
    R = w
    B = int(h/2)
    Y = pic.crop((L, T, R, B))
    Y = Y.transpose(Image.ROTATE_270)
    Y = Y.crop((0, 0, R//4, B//2))
    Y = Y.resize((w_b,h_b))    
    L = 0
    T = h//2
    R = w//2
    B = h  
    Bl = pic.crop((L, T, R, B))
    Bl = Bl.transpose(Image.ROTATE_90)
    Bl = Bl.crop((R//2, 0, R, B//4))
    Bl = Bl.resize((w_b,h_b))    
    L = w//2
    T = h//2
    R = w
    B = h     
    Rd = pic.crop((L, T, R, B)) 
    Rd = Rd.crop((0, 0, R//2, B//4))
    Rd = Rd.resize((w_b,h_b))
    imagee.paste(Rd, (0, 0))                 
    imagee.paste(Bl, (w // 2, 0))         
    imagee.paste(Y, (0, h // 2))         
    imagee.paste(G, (w // 2, h // 2))        
    imagee.show()
    return imagee

fix_frame(picture)