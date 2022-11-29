from rest_framework import serializers

from accounts.api.serializers import UserSerializer


from  core.models import Account,TransactionCharge,TransactionType,Transfer,Withdraw

class AccountSerializer(serializers.ModelSerializer):

	class Meta:

		model = Account
		fields = '__all__'

		extra_kwargs = {
			'pin_code':{
				'write_only':True
			}
		}
class AccountListSerializer(AccountSerializer):

	user = UserSerializer()

	class Meta:

		model = Account
		fields = '__all__'

class ChangePinSerializer(serializers.Serializer):

	old_pin = serializers.CharField(max_length=50,help_text='The old pin account')
	new_pin = serializers.CharField(max_length=50,help_text='The new pin account')
	confirm_pin = serializers.CharField(max_length=50,help_text='The confirm new pin account')

	class Meta:
		extra_kwargs = {
			'old_pin':{
				'required':True
			},
			'new_pin':{
				'required':True
			},'confirm_pin':{
				'required':True
			}
		}

class TransactionTypeSerializer(serializers.ModelSerializer):

	class Meta:
		model = TransactionType	
		fields = '__all__'

class TransactionListChargeSerializer(serializers.ModelSerializer):

	type = TransactionTypeSerializer()

	class Meta:
		model = TransactionCharge
		fields = '__all__'

class TransactionChargeSerializer(serializers.ModelSerializer):

	class Meta:

		model = TransactionCharge
		fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):

	class Meta:
		model = Transfer
		fields = '__all__'

class TransferListSerializer(TransferSerializer):

	sender = AccountSerializer()
	reciever = AccountSerializer()
	charge = TransactionListChargeSerializer()

class WithdrawSerializer(serializers.ModelSerializer):

	class Meta:
		model = Withdraw
		fields = '__all__'

		extra_kwargs = {
			'state':{
				'required':False
			}
		}

class WithdrawListSerializer(WithdrawSerializer):

	withdraw_from = AccountSerializer()
	agent= AccountSerializer()
	withdraw_charge = TransactionListChargeSerializer()
