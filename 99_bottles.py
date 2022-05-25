"""
function bottlesOfBeer() {
  
    for (let i = 99; i >= 2; i--){
      console.log(i + ' bottles of beer on the wall, ' + i + 'bottles of beer. Take one down, pass it around, ' + (i-1) + ' bottles of beer on the wall.')
    }
    console.log('Take one down and pass it around, 1 bottle of beer on the wall. 1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, \
    no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')
  }
  bottlesOfBeer()
"""



def bottle_song():
	# write your code here!
	refrain = " "
	for x in range(10,2,-1):
		print(f"{x} bottles of beer on the wall, {x} bottles of beer. Take one down, pass it around, {x-1} bottles of beer on the wall.")
		
	print("2 bottles of beer on the wall, 2 bottles of beer, Take one down, pass it around, 1 bottle of beer of the wall. 1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around,  no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song()
