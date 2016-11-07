FPATH="/home/rajiv/Documents/Kyle/inference_engine2/inference2/Proofs/5_7_16.py "
MYSQL=$(grep "mysql =" $FPATH | cut -d'=' -f2)
if [ "$MYSQL" = "False" ]; then
	echo "False"
fi