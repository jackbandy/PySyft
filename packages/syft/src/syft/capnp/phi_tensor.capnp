@0x8f9c60bd7a9842fc;
using Array = import "array.capnp".Array;

struct PT {
  magicHeader @0 :Data;
  child @1 :List(Data);
  minVals @2 :Data;
  maxVals @3 :Data;
  dataSubjectsIndexed @4 :Array;
  oneHotLookup @5 :Array;
}