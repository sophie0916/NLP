
public class FeatureSet {

	String word = "";
	String POS = "";
	String BIO = "";
	String stemmedVersion = "";
	String previousWord = "";
	String previousPOS = "";
	String twoWordsBack = "";
	String followingWord = "";
	String followingPOS = "";
	String twoWordsForward = "";
	boolean isCapital = false;
	boolean capitalized = false;
	boolean isAlpha = true;
	boolean isLine = false;
	boolean hasSpecial = false;

	public FeatureSet(){}

	public FeatureSet(String word, String POS, String BIO) {
		this.word = word;
		this.POS = POS;
		this.BIO = BIO;
	}

	public FeatureSet(String word, String POS) {
		this.word = word;
		this.POS = POS;
	}

	public void setPrevious(String previousWord, String previousPOS) {
		this.previousWord = previousWord;
		this.previousPOS = previousPOS;
	}

	public void setFollowing(String followingWord, String followingPOS) {
		this.followingWord = followingWord;
		this.followingPOS = followingPOS;
	}

	public String getPrevious(){
		String prev = "";
		prev += "two_words_back=" + this.twoWordsBack + "\t" + "previous_word=" + this.previousWord + "\t" + "previous_POS=" + this.previousPOS + "\t";
		return prev;
	}

	public String getFollowing(){
		String fol = "";
		fol += "following_word=" + this.followingWord + "\t" + "two_words_forward=" + this.twoWordsForward + "\t" + "following_POS=" + this.followingPOS + "\t";
		return fol;
	}



}
