FPATH="/home/rajiv/Documents/Kyle/inference_engine2/inference2/Proofs/prove.py "
MYSQL=$(grep "mysql =" $FPATH | cut -d'=' -f2)
if [ "$MYSQL" = "False" ]; then
	echo "False"
fi