"""
Static FAQ dataset based on ICICI Prudential Life Insurance
financial transactions knowledge base.
"""

FAQ_DATA = """
ICICI Prudential Life Insurance - Financial Transactions FAQ

=== PREMIUM PAYMENT ===

Q: How can I pay my premium online?
A: You can pay your premium online through multiple channels:
1. ICICI Prudential website (iciciprulife.com) using NetBanking, Credit/Debit Card, or UPI
2. ICICI Bank NetBanking
3. NEFT/RTGS transfer to the designated account
4. Auto-debit (ECS/NACH) from your registered bank account
5. Mobile app - iPruTouch
6. Payment through authorized agents or branches

Q: What happens if I miss a premium payment?
A: If you miss a premium payment, a grace period is provided:
- 30 days grace period for annual, semi-annual, and quarterly premium payments
- 15 days grace period for monthly premium payments
During the grace period, your policy remains active. If premium is not paid within the grace period, the policy may lapse.

Q: Can I pay premium for multiple policies in one transaction?
A: Yes, you can pay premiums for multiple policies in a single transaction using the ICICI Prudential website or mobile app. Select all the policies you wish to pay for and make a consolidated payment.

Q: What is the due date for premium payment?
A: The premium due date is the anniversary date of your policy. You can find the exact due date on your policy document, premium notice, or by logging into your account on iciciprulife.com.

Q: Is there a late payment fee?
A: There is no late payment fee if you pay within the grace period. However, if the policy lapses, revival charges may apply.

=== BANK ACCOUNT CHANGE ===

Q: How do I change my registered bank account?
A: To change your registered bank account:
1. Log in to iciciprulife.com or the iPruTouch app
2. Go to 'Service Requests' and select 'Change Bank Account'
3. Submit the required documents: cancelled cheque or bank statement of the new account
4. The request will be processed within 7-10 working days
You can also submit the request at the nearest ICICI Prudential branch.

Q: Is there any charge for changing my bank account?
A: No, there is no charge for updating your registered bank account details.

Q: What documents are required for bank account change?
A: The following documents are required:
- Cancelled cheque of the new bank account (with your name printed on it), OR
- Latest bank statement (not older than 3 months) showing your name and account details
- Self-attested copy of identity proof (if name on new account differs)

Q: How long does it take to update my bank account?
A: Bank account changes are typically processed within 7-10 working days from the date of receipt of complete documents.

=== FUND SWITCHING (UNIT LINKED POLICIES) ===

Q: How can I switch funds in my ULIP policy?
A: You can switch funds in your ULIP policy through:
1. Online: Log in to iciciprulife.com and go to 'Service Requests' > 'Fund Switch'
2. Mobile App: Use the iPruTouch app
3. Branch: Visit any ICICI Prudential branch
4. Written request: Submit a signed fund switch form to the nearest branch

Q: Is there a charge for switching funds?
A: A limited number of free fund switches are available per policy year (typically 4 free switches). Beyond that, a nominal switch fee applies. Please refer to your policy document for exact details.

Q: What is the cut-off time for fund switching?
A: Fund switch requests received before 3:00 PM on a business day are processed at the NAV of the same day. Requests received after 3:00 PM are processed at the next business day's NAV.

=== PARTIAL WITHDRAWAL ===

Q: Can I make a partial withdrawal from my policy?
A: Partial withdrawals are available in Unit Linked Insurance Plans (ULIPs) after the completion of the 5-year lock-in period. Traditional endowment or term plans generally do not allow partial withdrawals. The minimum partial withdrawal amount and maximum limits are specified in your policy document.

Q: How do I request a partial withdrawal?
A: To request a partial withdrawal:
1. Log in to iciciprulife.com or the iPruTouch app
2. Navigate to 'Service Requests' > 'Partial Withdrawal'
3. Enter the withdrawal amount
4. Confirm and submit
The amount will be credited to your registered bank account within 7 working days.

Q: Is partial withdrawal amount taxable?
A: Partial withdrawals from ULIPs are generally tax-free under Section 10(10D) of the Income Tax Act, subject to conditions. Please consult a tax advisor for personalized advice.

=== LOAN AGAINST POLICY ===

Q: Can I take a loan against my life insurance policy?
A: Yes, loans are available against traditional endowment and whole life policies that have acquired a surrender value. ULIPs and term plans are generally not eligible for policy loans.

Q: What is the maximum loan amount I can get?
A: The maximum loan amount is typically up to 85-90% of the surrender value of the policy. The exact amount depends on the policy type and terms.

Q: What is the interest rate on policy loans?
A: The interest rate on policy loans is specified in your policy document and may vary. Please contact ICICI Prudential customer care or visit a branch for current rates.

=== SURRENDER / FORECLOSURE ===

Q: What is policy surrender?
A: Policy surrender means terminating your policy before the maturity date and receiving the surrender value. The surrender value is the amount payable to you upon surrendering the policy.

Q: When can I surrender my policy?
A: For traditional policies, surrender is allowed after the policy has been in force for at least 3 years. For ULIPs, surrender is allowed after the 5-year lock-in period.

Q: Will I lose money if I surrender my policy?
A: Yes, surrendering a policy early may result in a loss as the surrender value is typically less than the total premiums paid. There may also be tax implications. It is advisable to consult with your financial advisor before surrendering.

=== CLAIM PROCESS ===

Q: How do I file a death claim?
A: To file a death claim:
1. Notify ICICI Prudential immediately by calling 1860-266-7766 or emailing claimsservicing@iciciprulife.com
2. Submit the claim form along with:
   - Original policy document
   - Death certificate (original or certified copy)
   - Identity and address proof of the nominee
   - Bank details of the nominee
3. Additional documents may be required based on the cause of death

Q: How long does it take to settle a claim?
A: ICICI Prudential aims to settle claims within 30 days of receipt of all required documents. Complex claims may take longer.

Q: What is the claim settlement ratio of ICICI Prudential?
A: ICICI Prudential Life Insurance has one of the highest claim settlement ratios in the industry, consistently above 98%. The exact current ratio can be found on the company website or IRDAI reports.

=== MATURITY PROCEEDS ===

Q: How will I receive my maturity amount?
A: The maturity amount is directly credited to your registered bank account. You should ensure your bank account details are up-to-date at least 30 days before maturity.

Q: Are maturity proceeds taxable?
A: Maturity proceeds are generally exempt from income tax under Section 10(10D) of the Income Tax Act, subject to certain conditions (such as the premium not exceeding 10% of the sum assured). Please consult a tax advisor for specific advice.

=== CONTACT & SUPPORT ===

Q: How can I contact ICICI Prudential customer care?
A: You can reach ICICI Prudential through:
- Phone: 1860-266-7766 (Monday to Saturday, 9 AM to 7 PM)
- Email: lifeline@iciciprulife.com
- Chat: Available on iciciprulife.com
- Branch: Visit the nearest ICICI Prudential branch
- WhatsApp: Send 'Hi' to +91 8655550009

Q: How do I update my contact details?
A: You can update your contact details (mobile number, email address) by:
1. Logging in to iciciprulife.com
2. Going to 'Profile' > 'Update Contact Details'
3. Verifying with OTP
Or by visiting the nearest branch with identity proof.

Q: What is the free look period?
A: The free look period is 15 days from the date of receipt of the policy document (30 days for policies sold through distance marketing). During this period, you can return the policy if you are not satisfied, and receive a refund of the premium paid after deducting risk premium and administrative charges.
"""