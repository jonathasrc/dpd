
def lineIDDA(img , yi, xi, yf, xf, vetor):

  rows, cols = img.shape[:2]
  erro, q = 0, 0
  quantidade = 0
  deltax = xf - xi
  deltay = yf - yi
  list_vertices = []

  # When ys > ye the line is diagnoal to down. For this is
  # necessary invert the points
  # When deltax = 0 and deltay < 0, the line is in vertical
  # to down. For this is necessary invert ys with ye
  if((yi > yf) or ((deltax == 0) and (deltay < 0))):
    invert(xi, xf)
    invert(yi, yf)
    deltax = xf - xi
    deltay = yf - xi

  x = xi
  y = yi

  # 'quant' denotes the maximum number of ploted points
  if (abs(deltax) > abs(deltay)):
    quantidade = abs(deltax)
  else:
    quantidae = abs(deltay) 
  
  get_point = True
  entered = False
  finished = False
  walk = 1000 # clean more pixels
  try: 
    
    while q <= quantidade and walk: # While have points to plot

      if(x >= 0 and y >= 0 and x < cols and y < rows):
        
        if(not entered and img[y, x] == 0):  # find a spiral
          entered = True
          if(get_point):
            get_point = False
            vert.x = x
            vert.y = y
            list_vertices.append(vert)
          
          img[y, x] = 255

      if(entered):
        walk -= 1
        if(x >= 0 and y >= 0 and x < cols and y < rows):
          img[y, x] = 255 # Set the color white to avoid reprocessings

      if((deltax >= 0) and (deltay >= 0) and (deltax >= deltay)): # 1 oct
        if((erro < 0) or (deltay == 0)):
          x += 1
          erro = erro + deltay
        else:
          x += 1
          y += 1
          erro = erro + deltay - deltax
      elif ((deltax >= 0) and (deltay >= 0) and (deltay > deltax)): # 2 oct
        if (erro < 0):
          x += 1
          y += 1
          erro = erro + deltay - deltax
        else:
          y += 1
          erro = erro - deltax
      elif ((deltay >= 0) and (deltax < 0) and (-deltax >= deltay)): # 4 oct
        if((erro < 0) or (deltay == 0)):
          x += 1
          erro = erro + deltay
        else:
          x -= 1
          y += 1
          erro = erro + deltax + deltay
      elif ((deltay > 0) and (deltax < 0) and (deltay > -deltax)): # 3 oct
        if(erro < 0): 
          x -= 1
          y += 1
          erro = erro + deltax + deltay
        else:
          y += 1
          erro = erro + deltax
      elif ((deltay > 0) and (deltax < 0) and (deltay > -deltax)): # 8 oct
        if(erro < 0): 
          x -= 1
          erro = erro + deltay
        else:
          x += 1
          y -= 1
          erro = erro + abs(deltay) - deltax
      elif ((deltax >= 0) and (deltay < 0) and (-deltay > deltax)): # 7 oct
        if(erro < 0): 
          x += 1
          y -= 1
          erro = erro - deltay - deltax
        else:
          y -= 1
          erro = erro - deltax
      elif ((deltay < 0) and (deltax < 0) and (-deltay > -deltax)): # 3 oct
        if(erro < 0): 
          x -= 1
          y -= 1
          erro = erro + deltax - deltay
        else:
          y -= 1
          erro = erro + deltax
      elif ((deltay < 0) and (deltax < 0) and (-deltax >= -deltay)): # 4 oct
        if(erro < 0):
          x -= 1
          erro = erro - deltay
        else:
          x -= 1
          y += 1
          erro = erro + deltax - deltay
    
      q += int(1)
  except:
    print(f'Something else went wrong walk = {walk}, quantidade = {quantidade}')
    