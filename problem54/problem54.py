values = dict({str(i):i for i in range(2, 10)}, **{'T':10, 'J':11, 'Q':12, 'K':13, 'A':14})
straights = [list(range(x, x+5)) for x in range(2,11)] + [[2,3,4,5,14]]

def parse_hands(hh): return list(map(lambda h: (values[h[0]], h[1]), hh))
def straight(hand): return (5, max(hand)[0]) if sorted([i[0] for i in hand]) in straights else False
def flush(hand): return (6, max(hand, key=lambda x: x[0])[0]) if len(set([i[1] for i in hand]))==1 else False
def highcard(hand, card, prev=False): return list(set(hand) - {card, prev})[0] if prev else max(set(hand) - {card})

'''
	Point Guide:
		- 10: Royal Flush
		-  9: Straight Flush
		-  8: Four of a Kind
		-  7: Full House
		-  6: Flush
		-  5: Straight
		-  4: Three of a Kind
		-  3: Two Pairs
		-  2: One Pair
		-  1: High Card
'''

def point(hand):
	hand = list(map(lambda card: card[0], hand))
	if len(set(hand))==5: return (1, max(hand))
	
	pair, three = False, False
	for card in set(hand):
		if hand.count(card)==2:
			if pair:
				return (3, (pair[1], card), highcard(hand, card, pair[1]))
			elif three:
				return (7, (three[1], card))
			else:
				pair = (2, card, highcard(hand, card))
		elif hand.count(card)==3:
			if pair:
				return (7, (card, pair[1]))
			else:
				three = (4, card, highcard(hand, card))
		elif hand.count(card)==4:
			return (8, card)
	return pair if pair else three

def get_point(points):
	return (9, points[0][1]) if points[0] and points[1] else max(filter(lambda x: x, points), key=lambda x: x[0])

def check(handgames):
	handgames = [parse_hands(handgames[0]), parse_hands(handgames[1])]
	
	hand0 = get_point([straight(handgames[0]), flush(handgames[0]), point(handgames[0])])
	hand1 = get_point([straight(handgames[1]), flush(handgames[1]), point(handgames[1])])
	
	#if player got the same point, return as winner the hand with higher card
	return hand0[0] > hand1[0] if hand0[0] != hand1[0] else hand0[1] > hand1[1]

if __name__ == '__main__':
	games = open('poker.txt', 'r').readlines()
	games = [i.strip().split() for i in games]
	games = map(lambda r: [tuple(list(i)) for i in r], games)
	games = map(lambda r: [r[:5],r[5:]], games)

	player1, player2 = 0, 0

	for game in games:
		if check(game):
			player1 += 1
		else:
			player2 += 1
	
	#print('Player1:', player1)
	#print('Player2:', player2)
	print('Result:', player1)



