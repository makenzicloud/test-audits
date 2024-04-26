-include .env

.PHONY: all test clean deploy fund help install snapshot format anvil append-counterexamples

DEFAULT_ANVIL_KEY := 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

all:  remove install build

# Clean the repo
clean  :; forge clean

# Remove modules
remove :; rm -rf .gitmodules && rm -rf .git/modules/* && rm -rf lib && touch .gitmodules && git add . && git commit -m "modules"

install :; forge install foundry-rs/forge-std --no-commit 

# Update Dependencies
update:; forge update

build:; forge build

test :; forge test 

snapshot :; forge snapshot

format :; forge fmt

anvil :; anvil -m 'test test test test test test test test test test test junk' --steps-tracing --block-time 1

coverage :; forge coverage 

certora :; certora run

coverage-report :; forge coverage --report debug > coverage-report.txt

scope :; tree ./src/ | sed 's/└/#/g; s/──/--/g; s/├/#/g; s/│ /|/g; s/│/|/g'

scopefile :; @tree ./src/ | sed 's/└/#/g' | awk -F '── ' '!/\.sol$$/ { path[int((length($$0) - length($$2))/2)] = $$2; next } { p = "src"; for(i=2; i<=int((length($$0) - length($$2))/2); i++) if (path[i] != "") p = p "/" path[i]; print p "/" $$2; }' > scope.txt

slither :; slither . --config-file slither.config.json 

aderyn :; aderyn . 
###########################################################################################################

default: help

SRC   := ../contracts
DST   := patched
DIFF  := diff
SRCS  := $(shell find $(SRC) -type f)
DSTS  := $(shell find $(DST) -type f)
DIFFS := $(shell find $(DIFF) -type f)

###############################################################################
# Apply all patches in the $DIFF folder to the $DST folder
apply: $(DST) $(patsubst $(DIFF)/%.patch,$(DST)/%,$(subst _,/,$(DIFFS)))

# Reset the $DST folder
$(DST): FORCE
	@rm -rf $@
	@cp -r $(SRC) $@

# Update a solidity file in the $DST directory using the corresponding patch
$(DST)/%.sol: FORCE
	@echo Applying patch to $@
	@patch -p0 -d $(DST) < $(patsubst $(DST)_%,$(DIFF)/%.patch,$(subst /,_,$@))

###############################################################################
# Record all difference between $SRC and $DST in patches
record: $(DIFF) $(patsubst %,$(DIFF)/%.patch,$(subst /,_,$(subst $(SRC)/,,$(SRCS)) $(subst $(DST)/,,$(DSTS))))

# Create the $DIFF folder
$(DIFF): FORCE
	@rm -rf $@
	@mkdir $@

# Create the patch file by comparing the source and the destination
$(DIFF)/%.patch: FORCE
	@echo Generating patch $@
	@diff -ruN \
		$(patsubst $(DIFF)/%.patch,$(SRC)/%,$(subst _,/,$@)) \
		$(patsubst $(DIFF)/%.patch,$(DST)/%,$(subst _,/,$@)) \
		| sed 's+$(SRC)/++g' \
		| sed 's+$(DST)/++g' \
		> $@
	@[ -s $@ ] || rm $@

###############################################################################
help:
	@echo "usage:"
	@echo "  make apply:  create $(DST) directory by applying the patches to $(SRC)"
	@echo "  make record: record the patches capturing the differences between $(SRC) and $(DST)"
	@echo "  make clean:  remove all generated files (those ignored by git)"

clean:
	git clean -fdX

FORCE: ;
