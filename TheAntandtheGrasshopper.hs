data Season = Summer | Winter deriving Show
data Character = Ant { workDone :: Int } | Grasshopper { playTime :: Int } deriving Show

surviveWinter :: Season -> Character -> Bool
surviveWinter Winter (Ant work) = work > 10
surviveWinter Winter (Grasshopper play) = False
surviveWinter _ _ = True

-- Ant worked hard during the summer.
ant = Ant 12
-- Grasshopper played all summer long.
grasshopper = Grasshopper 12

main = do
  print $ surviveWinter Winter ant
  print $ surviveWinter Winter grasshopper
